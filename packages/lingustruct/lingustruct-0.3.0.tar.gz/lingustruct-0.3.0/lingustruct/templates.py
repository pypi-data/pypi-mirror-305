import json
import os
import logging  # ロギングモジュールのインポート
from typing import Dict, Set

# ロガーの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 必要に応じてログレベルを設定
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")


def load_template(template_name: str) -> dict:
    """
    指定されたテンプレート名のJSONファイルをロードする。
    
    Args:
        template_name (str): ロードするテンプレートの名前（拡張子なし）。
    
    Returns:
        dict: テンプレートの内容。
    
    Raises:
        FileNotFoundError: テンプレートファイルが存在しない場合。
        json.JSONDecodeError: JSONのパースに失敗した場合。
    """
    file_path = os.path.join(TEMPLATE_DIR, f"{template_name}.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{template_name}.json が見つかりません。")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def calculate_match_score(data_keys: Set[str], template_fields: Dict) -> int:
    """
    データキーとテンプレートフィールドの一致数を計算
    
    Args:
        data_keys (Set[str]): データのキーの集合。
        template_fields (Dict): テンプレートのフィールド情報。
    
    Returns:
        int: 一致数。
    """
    template_keys = set(template_fields.keys())
    score = len(data_keys & template_keys)
    logger.debug(f"Matching {data_keys} with {template_keys}: Score {score}")
    return score


def auto_detect_template(data: Dict) -> str:
    """
    データのキーに基づいて最適なテンプレートを自動選択
    
    Args:
        data (Dict): マッピング対象のデータ。
    
    Returns:
        str: 選択されたテンプレートの名前。
    
    Raises:
        ValueError: 適切なテンプレートが見つからない場合。
    """
    if not data:
        raise ValueError("入力データが空です。少なくとも1つのフィールドを提供してください。")
    
    best_match = None
    highest_score = 0

    for template_file in os.listdir(TEMPLATE_DIR):
        if template_file.endswith(".json"):
            template_name = template_file.replace(".json", "")
            try:
                template = load_template(template_name)
                score = calculate_match_score(set(data.keys()), template.get("fields", {}))
                logger.debug(f"Template '{template_name}' score: {score}")
                if score > highest_score:
                    highest_score = score
                    best_match = template_name
            except Exception as e:
                logger.error(f"Error loading template '{template_name}': {str(e)}")

    if not best_match:
        raise ValueError("適切なテンプレートが見つかりません。")

    return best_match


class TemplateManager:
    def __init__(self, data_path='lingustruct/data/data.json'):
        self.data_path = data_path
        self.templates = self.load_templates()
        # 自動マッピング用テンプレートの読み込み
        self.auto_mapping_templates = self.load_auto_mapping_templates()

    def load_templates(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"{self.data_path} が見つかりません。")
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('fields', [])

    def load_auto_mapping_templates(self) -> Dict[str, dict]:
        """
        テンプレートディレクトリから全テンプレートをロードする。
        
        Returns:
            Dict[str, dict]: テンプレート名をキーとしたテンプレート内容の辞書。
        """
        templates = {}
        for template_file in os.listdir(TEMPLATE_DIR):
            if template_file.endswith(".json"):
                template_name = template_file.replace(".json", "")
                try:
                    templates[template_name] = load_template(template_name)
                    logger.debug(f"Loaded template: {template_name}")
                except Exception as e:
                    logger.error(f"Failed to load template {template_name}: {str(e)}")
        return templates

    def get_field(self, field_name: str):
        for field in self.templates:
            if field['name'] == field_name:
                return field
        return None

    def add_field(self, field: dict):
        self.templates.append(field)
        self.save_templates()

    def save_templates(self):
        with open(self.data_path, 'w', encoding='utf-8') as f:
            json.dump({"fields": self.templates}, f, ensure_ascii=False, indent=4)

    def auto_map_data(self, data: dict) -> dict:
        """
        データを自動的に最適なテンプレートへマッピング
        
        Args:
            data (dict): マッピング対象のデータ。
        
        Returns:
            dict: 選択されたテンプレート名とマッピングされたデータ。
        
        Raises:
            ValueError: 適切なテンプレートが見つからない場合。
        """
        template_name = auto_detect_template(data)
        template = self.auto_mapping_templates.get(template_name)

        if not template:
            raise ValueError(f"テンプレート '{template_name}' がロードされていません。")

        # テンプレートのフィールドからラベルとキーのマッピングを作成
        mapping = {field_info["label"]: key for key, field_info in template.get("fields", {}).items()}
        mapped_data = {mapping.get(k, k): v for k, v in data.items()}

        return {"template": template_name, "mapped_data": mapped_data}
