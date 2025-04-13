from fpdf import FPDF
import datetime
import platform
import socket
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Ransomware Simulation Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "System Name": platform.node(),
        "Username": os.getlogin(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
    }

def generate_pdf_report():
    pdf = PDFReport()
    pdf.add_page()
    
    # Set default font (Arial)
    pdf.set_font("Arial", "", 12)

    # Report Date
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(0, 10, f"Report Generated on: {now}", ln=True)
    pdf.ln(5)

    # System Information
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "System Information:", ln=True)
    pdf.set_font("Arial", "", 10)
    system_info = get_system_info()
    for key, value in system_info.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)
    pdf.ln(5)

    # Read log file
    try:
        with open("log.txt", "r", encoding="utf-8") as log_file:
            lines = log_file.readlines()
    except FileNotFoundError:
        pdf.cell(0, 10, "No log file found. Run encryption and decryption first.", ln=True)
        pdf.output("ransomware_report.pdf")
        print("Report generated: ransomware_report.pdf")
        return

    # Parse log data for summary statistics
    encrypted_files = [line.strip() for line in lines if line.startswith("Encrypted:")]
    decrypted_files = [line.strip() for line in lines if line.startswith("Decrypted:")]

    # Summary Section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Summary", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Total Files Encrypted: {len(encrypted_files)}", ln=True)
    pdf.cell(0, 10, f"Total Files Decrypted: {len(decrypted_files)}", ln=True)
    pdf.ln(5)

    # Detailed Log of Encrypted Files
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Encrypted Files:", ln=True)
    pdf.set_font("Arial", "", 10)
    if encrypted_files:
        for line in encrypted_files:
            pdf.multi_cell(0, 10, f"{line}")
    else:
        pdf.cell(0, 10, "No encrypted files found.", ln=True)
    pdf.ln(5)

    # Detailed Log of Decrypted Files
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Decrypted Files:", ln=True)
    pdf.set_font("Arial", "", 10)
    if decrypted_files:
        for line in decrypted_files:
            pdf.multi_cell(0, 10, f"{line}")
    else:
        pdf.cell(0, 10, "No decrypted files found.", ln=True)
    
    pdf.ln(5)

    # Security Analysis & Recommendations
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Security Analysis & Recommendations:", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 10, 
        "This simulation demonstrates how ransomware encrypts files.\n\n"
        "To protect against real ransomware attacks:\n"
        "  1. Keep systems and software updated.\n"
        "  2. Use endpoint protection and firewalls.\n"
        "  3. Backup critical files regularly.\n"
        "  4. Avoid opening suspicious links or email attachments.\n"
        "  5. Implement strong access controls.\n"
        "Always test ransomware simulations in a safe environment!"
    )

    pdf.output("ransomware_report.pdf")
    print("Report generated: ransomware_report.pdf")

# Run the report generator
generate_pdf_report()
