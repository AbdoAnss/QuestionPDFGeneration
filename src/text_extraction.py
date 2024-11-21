import os
import re
import json
import jinja2
import pdfkit


class QuestionPDFGenerator:
    def __init__(
        self,
        input_txt_file="data/input/web.txt",
        output_json="data/output/extracted_data.json",
        html_template="templates/qcm.html",
        css_file="templates/qcm.css",
        output_pdf="data/output/qcm.pdf",
    ):
        """
        Initialize PDF generation process with configurable paths
        """
        # Ensure output directories exist
        os.makedirs(os.path.dirname(output_json), exist_ok=True)
        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        self.input_txt_file = input_txt_file
        self.output_json = output_json
        self.html_template = html_template
        self.css_file = css_file
        self.output_pdf = output_pdf

        # Title for the document
        self.title = "AHA PALS EXAM 2024 ACTUAL EXAM TEST BANK 230 QUESTIONS AND CORRECT DETAILED ANSWERS WITH RATIONALES"

    def extract_questions_with_answers(self, text):
        """
        Extract questions, options, and answers from text
        """
        blocks = text.split("DEFINITION")
        extracted_data = []

        for block in blocks:
            # Extract question
            question_match = re.search(r"\d+\.\s(.*?)(?=\nA\.)", block, re.DOTALL)
            if not question_match:
                continue
            question = question_match.group(1).strip()

            # Extract options
            options = re.findall(r"[A-D]\.\s.*", block)

            # Extract answer
            answer_match = re.search(
                r"TERM.*?\n.*?\nImage\n\n\n\n(.*)", block, re.DOTALL
            )
            answer = (
                answer_match.group(1).strip() if answer_match else "Answer not found"
            )

            extracted_data.append({
                "question": question,
                "options": options,
                "answer": answer,
            })

        return extracted_data

    def generate_json(self, extracted_data):
        """
        Generate JSON file from extracted data
        """
        with open(self.output_json, "w") as json_file:
            json.dump(extracted_data, json_file, indent=4)
        print(f"JSON file saved to {self.output_json}")

    def generate_pdf(self):
        """
        Generate PDF using Jinja2 template and pdfkit
        """
        # Validate files exist
        if not all(
            os.path.exists(path)
            for path in [self.input_txt_file, self.html_template, self.css_file]
        ):
            raise FileNotFoundError("One or more required files are missing")

        # Read input file
        with open(self.input_txt_file, "r") as file:
            content = file.read()

        # Extract questions
        questions = self.extract_questions_with_answers(content)

        # Generate JSON
        self.generate_json(questions)

        # Load the template
        template_loader = jinja2.FileSystemLoader("./")
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(self.html_template)

        # Render the template with the question data
        output_text = template.render(title=self.title, questions=questions)

        # Configure pdfkit
        wkhtmltopdf_paths = [
            "/usr/bin/wkhtmltopdf",  # Linux
            "/usr/local/bin/wkhtmltopdf",  # macOS
            "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe",  # Windows
        ]

        wkhtmltopdf_path = next(
            (path for path in wkhtmltopdf_paths if os.path.exists(path)), None
        )

        if not wkhtmltopdf_path:
            raise FileNotFoundError("wkhtmltopdf not found. Please install it.")

        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Generate the PDF
        pdfkit.from_string(
            output_text, self.output_pdf, configuration=config, css=self.css_file
        )
        print(f"PDF generated: {self.output_pdf}")


def main():
    """
    Main entry point for the script
    """
    try:
        # Create PDF generator instance
        pdf_generator = QuestionPDFGenerator()

        # Process extraction and PDF generation
        pdf_generator.generate_pdf()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
