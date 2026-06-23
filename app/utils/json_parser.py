import json
import re


class JsonParser:

    @staticmethod
    def parse_response(response):

        try:

            match = re.search(
                r"\{.*\}",
                response,
                re.DOTALL
            )

            if not match:
                return None

            json_string = match.group()

            return json.loads(json_string)

        except Exception:

            return None