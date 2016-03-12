from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def print_html_doc():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

    with open('testresults.html', 'r') as myfile:
        table_data=myfile.read()

    portal_url = "https://elementsportal.sps.comcast.net"
    jenkins_build_status = "http://www.google.com"
    github_url = "https://github.comcast.com/XPlat/Elements_portal"
    github_url = "https://github.comcast.com/XPlat/Elements_portal/1"

    print j2_env.get_template('test_temp.html').render(
            title='Hellow Gist from GutHub',
            url="http://www.google.com",
            name="mike"
    )

if __name__ == '__main__':
    print_html_doc()