import datetime
import os
import random
import string

import pypandoc


class ConversionUtility:
    def __init__(self):
        pass

    @staticmethod
    def html_to_pdf_file(body="", css_file=""):
        now = datetime.datetime.now()
        random_string = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        tempfile = "/tmp/seedoo-temp-%s-%s.pdf" % (now.strftime("%Y%m%d%H%M%S"), random_string)

        extra_args = ["--standalone", "--latex-engine=pdflatex"]

        if css_file and len(css_file) > 0 and os.path.isfile(css_file):
            extra_args.append("--css=%s" % css_file)

        pypandoc.convert(
            body,
            "html5",
            outputfile=tempfile,
            format="html",
            extra_args=extra_args)

        return tempfile

    @staticmethod
    def html_to_pdf(body="", css_file=""):
        tempfile = ConversionUtility.html_to_pdf_file(body=body, css_file=css_file)

        with file(tempfile) as tmpf:
            pdf_content = tmpf.read()

        os.remove(tempfile)
        return pdf_content
