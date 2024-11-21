from src.text_extraction import QuestionPDFGenerator


def main():
    """
    Main entry point to run the entire extraction and PDF generation process
    """
    try:
        # Create PDF generator instance with default or custom paths
        pdf_generator = QuestionPDFGenerator(
            input_txt_file="data/input/web.txt",
            output_json="data/output/extracted_data.json",
            html_template="templates/qcm.html",
            css_file="templates/qcm.css",
            output_pdf="data/output/qcm.pdf",
        )

        # Process extraction and PDF generation
        pdf_generator.generate_pdf()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
