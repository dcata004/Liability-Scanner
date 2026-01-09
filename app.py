import gradio as gr
import requests
from bs4 import BeautifulSoup

def scan_terms(url):
    if not url:
        return "Please enter a URL.", "GRAY"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().lower()
        
        # Risk Keywords
        red_flags = [
            "perpetual license", 
            "irrevocable license", 
            "right to use", 
            "train our models",
            "improve our services",
            "royalty-free",
            "worldwide license"
        ]
        
        found_flags = [phrase for phrase in red_flags if phrase in text]
        
        if len(found_flags) > 0:
            return f"🚨 HIGH RISK DETECTED\n\nWe found clauses that may grant the vendor rights to your data:\n" + "\n".join([f"- '{f}'" for f in found_flags]), "RED"
        else:
            return "✅ NO OBVIOUS RED FLAGS FOUND\n\n(Note: This is an automated scan, not legal advice. Always review the full contract.)", "GREEN"

    except Exception as e:
        return f"Error scanning URL: {str(e)}", "GRAY"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📜 AI Liability Scanner")
    gr.Markdown("Paste a Vendor's 'Terms of Service' URL to scan for clauses that grant them the right to train on your data.")
    
    url_input = gr.Textbox(label="Terms of Service URL", placeholder="https://openai.com/policies/terms")
    scan_btn = gr.Button("Scan Contract", variant="primary")
    output_box = gr.Textbox(label="Risk Assessment")
    
    scan_btn.click(scan_terms, inputs=url_input, outputs=output_box)

demo.launch()
