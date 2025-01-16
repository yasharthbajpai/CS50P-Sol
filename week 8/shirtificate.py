from fpdf import FPDF

def create_shitificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", "B", 32)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C")

   
    pdf.image("shirtificate.png", x=10, y=60, w=190)

    
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255) 
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    
    pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    create_shitificate(name)
    print("Shirtificate created as 'shirtificate.pdf'")

if __name__ == "__main__":
    main()