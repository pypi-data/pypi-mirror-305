import json
from pydantic import BaseModel
from .utils import *
from .prompts import SCRAPER_GENERATOR_PROMPT, DATA_STRUCTURE_PROMPT


class GPTScraper:
    def __init__(self, source_code: str, data_structure: BaseModel = None):
        """
        The GPTScraper class is designed to parse HTML content using a source code parser
        and an optional data structure model.

        Args:
            source_code (str): The source code for parsing HTML content.
            data_structure (BaseModel, optional): A Pydantic model representing the data structure of the parsed output.
        """
        self.source_code = source_code
        self.parse = parser_from_text(source_code)
        self.data_structure = data_structure

    @classmethod
    def from_html(
            cls,
            page_source: str,
            requirements: str,
            data_structure: BaseModel = None,
            model_name: str = "gpt-4o",
    ) -> "GPTScraper":
        """
        Create a GPTScraper instance from HTML content and user requirements.

        Args:
            page_source (str): The HTML content of the webpage.
            requirements (str): The user-defined requirements for scraping.
            data_structure (BaseModel, optional): An optional data structure for the output.
            model_name (str): The model name to be used by the LLMProvider.

        Returns:
            GPTScraper: An instance of the GPTScraper class.
        """
        llm_provider = ProviderOpenAI(model_name)
        # prepare prompt
        system_prompt = SCRAPER_GENERATOR_PROMPT.replace(
            "{{USER_REQUIREMENTS}}", requirements
        )
        system_prompt = system_prompt.replace(
            "{{HTML_CODE}}", page_source
        )
        if data_structure is not None:
            data_structure_prompt = DATA_STRUCTURE_PROMPT.replace(
                "{{DATA_STRUCTURE}}", data_structure_to_str(data_structure)
            )
            system_prompt = system_prompt.replace(
                "{{EXTRA_REQUIREMENTS}}", data_structure_prompt
            )
        else:
            system_prompt = system_prompt.replace("{{EXTRA_REQUIREMENTS}}", "")
        # get response
        parser_code = llm_provider(system_prompt)
        parser_code = extract_code_block(parser_code)
        return cls(parser_code, data_structure)

    @classmethod
    def from_source_code(
            cls,
            source_code: str,
            data_structure: BaseModel = None
    ) -> "GPTScraper":
        """
        Create a GPTScraper instance from the given source code and data structure.

        Args:
            source_code (str): The source code for parsing HTML content.
            data_structure (BaseModel, optional): An optional data structure for the output.

        Returns:
            GPTScraper: An instance of the GPTScraper class.
        """
        return cls(source_code, data_structure)

    def save(self, path: str) -> None:
        """
        Save the source code of the parser to a file.

        Args:
            path (str): The path to save the source code.
        """
        with open(path, "w") as f:
            json.dump({"source_code": self.source_code}, f, indent=4)

    @classmethod
    def load(cls, path: str) -> "GPTScraper":
        """
        Load the source code of the parser from a file.

        Args:
            path (str): The path to load the source code from.

        Returns:
            GPTScraper: An instance of the GPTScraper class.
        """
        with open(path, "r") as f:
            data = json.load(f)
            source_code = data["source_code"]
            return cls(source_code)

    def parse_html(self, html: str):
        """
        Parse the provided HTML string into a structured format.

        Args:
            html (str): The HTML content to be parsed.

        Returns:
            list: A list of parsed data according to the data structure provided, if any.
        """
        output = self.parse(html)
        if self.data_structure is not None:
            return [self.data_structure(**item) for item in output]
        return output

    def check_parser(self, html: str) -> bool:
        """
        Check if the parser can successfully parse the HTML content without errors.

        Args:
            html (str): The HTML content to be parsed.

        Returns:
            bool: True if parsing is successful, otherwise False.
        """
        try:
            self.parse_html(html)
            return True
        except Exception as e:
            return False
