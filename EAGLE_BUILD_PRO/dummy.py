import json
import webbrowser
from pathlib import Path
import os
import subprocess

def generate_sample_profiles():
    profiles = [
        {
            "Use Case": "New Parents",
            "Client ID": "C001",
            "Name": "John & Lisa",
            "Age": 32,
            "Marital Status": "Married",
            "Children": 2,
            "Income (R)": 85000,
            "Occupation": "Engineer & Teacher",
            "Investment Products": "Mutual Funds",
            "Insurance Products": "None",
            "Risk Profile": "Moderate"
        },
        {
            "Use Case": "Young Professionals",
            "Client ID": "C002",
            "Name": "Maya P.",
            "Age": 27,
            "Marital Status": "Single",
            "Children": 0,
            "Income (R)": 72000,
            "Occupation": "Software Developer",
            "Investment Products": "Crypto, Tech ETFs",
            "Insurance Products": "None",
            "Risk Profile": "Aggressive"
        },
        {
            "Use Case": "Near Retirement",
            "Client ID": "C003",
            "Name": "Robert K.",
            "Age": 61,
            "Marital Status": "Married",
            "Children": 3,
            "Income (R)": 130000,
            "Occupation": "Retired Executive",
            "Investment Products": "Bonds, Fixed Deposits",
            "Insurance Products": "Term Life",
            "Risk Profile": "Conservative"
        },
        {
            "Use Case": "High Net Worth",
            "Client ID": "C004",
            "Name": "Evelyn S.",
            "Age": 48,
            "Marital Status": "Divorced",
            "Children": 1,
            "Income (R)": 380000,
            "Occupation": "Business Owner",
            "Investment Products": "Private Equity, REITs",
            "Insurance Products": "Whole Life",
            "Risk Profile": "Balanced"
        },
        {
            "Use Case": "No Insurance Coverage",
            "Client ID": "C005",
            "Name": "Ahmed Z.",
            "Age": 36,
            "Marital Status": "Married",
            "Children": 2,
            "Income (R)": 68000,
            "Occupation": "Accountant",
            "Investment Products": "None",
            "Insurance Products": "None",
            "Risk Profile": "Moderate"
        }
    ]
    return profiles

def create_landing_page():
    image_url = "https://images.pexels.com/photos/7735630/pexels-photo-7735630.jpeg?auto=compress&cs=tinysrgb&w=1200"
    background_url = "https://images.pexels.com/photos/8441854/pexels-photo-8441854.jpeg?auto=compress&cs=tinysrgb&w=1600"  # Soft, professional, finance/insurance themed
    landing_html = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Welcome</title>
        <link href='https://fonts.googleapis.com/css?family=Segoe+UI:400,700&display=swap' rel='stylesheet'>
        <style>
            html, body {{ height: 100%; margin: 0; padding: 0; }}
            body {{
                background: url('{background_url}') no-repeat center center fixed;
                background-size: cover;
                color: #eaeaea;
                font-family: 'Segoe UI', Arial, sans-serif;
                min-height: 100vh;
            }}
            header {{ background: #3a7ca5cc; color: #fff; padding: 24px 0; text-align: center; box-shadow: 0 2px 8px #222; }}
            nav {{ background: #222b; color: #eaeaea; text-align: center; padding: 12px 0; font-size: 1.1em; }}
            nav a {{ color: #eaeaea; text-decoration: none; margin: 0 16px; transition: color 0.2s, text-decoration 0.2s; cursor: pointer; }}
            nav a:hover {{ color: #3a7ca5; text-decoration: underline; }}
            .hero-img {{ width: 100%; max-height: 350px; object-fit: cover; border-bottom: 4px solid #3a7ca5; }}
            .container {{ max-width: 900px; margin: 40px auto 200px auto; text-align: center; padding: 32px; background: rgba(45,45,45,0.85); border-radius: 16px; box-shadow: 0 2px 16px #222; }}
            .btn {{ background: #3a7ca5; color: #eaeaea; border: none; padding: 16px 32px; font-size: 1.2em; cursor: pointer; border-radius: 8px; box-shadow: 0 2px 8px #222; transition: background 0.2s, color 0.2s, box-shadow 0.2s; margin-top: 32px; }}
            .btn:hover {{ background: #eaeaea; color: #3a7ca5; box-shadow: 0 4px 16px #3a7ca5; }}
            .footer {{ background: #222b; color: #eaeaea; text-align: center; padding: 20px 0; position: relative; left: 0; bottom: 0; width: 100%; font-size: 1em; margin-top: 100px; }}
        </style>
    </head>
    <body>
        <header>
            <h1>Insurance Client Segmentation</h1>
        </header>
        <nav>
            <a href='landing.html'>Home</a>
            <a href='sample_customer_profiles.html'>Customer Profiles</a>
            <a href='insights.html'>Insights</a>
            <a href='about.html'>About Us</a>
        </nav>
        <img src='{image_url}' alt='Insurance Theme' class='hero-img'/>
        <div class="container">
            <h2 style='color:#3a7ca5;'>Welcome to Insurance Client Segmentation</h2>
            <p>Unlock the power of data-driven marketing and personalized product recommendations.</p>
            <button class="btn" onclick="window.location.href='sample_customer_profiles.html'">View Customer Profiles</button>
            <button class="btn" onclick="window.location.href='insights.html'">View Insights</button>
            <button class="btn" onclick="window.location.href='about.html'">About Us</button>
            <div style='height:400px;'></div>
        </div>
        <div class="footer">
            &copy; 2025 Old Mutual Hackathon | Powered by Data-Driven Solutions
        </div>
    </body>
    </html>
    """
    Path("landing.html").write_text(landing_html, encoding="utf-8")

def create_profiles_page(sample_profiles):
    background_url = "https://images.pexels.com/photos/8441854/pexels-photo-8441854.jpeg?auto=compress&cs=tinysrgb&w=1600"
    html_path = Path("sample_customer_profiles.html")
    html_content = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Customer Profiles</title>
        <link href='https://fonts.googleapis.com/css?family=Segoe+UI:400,700&display=swap' rel='stylesheet'>
        <style>
            body {{
                background: url('{background_url}') no-repeat center center fixed;
                background-size: cover;
                color: #eaeaea;
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            header {{ background: #3a7ca5cc; color: #fff; padding: 24px 0; text-align: center; box-shadow: 0 2px 8px #222; }}
            nav {{ background: #222b; color: #eaeaea; text-align: center; padding: 12px 0; font-size: 1.1em; }}
            nav a {{ color: #eaeaea; text-decoration: none; margin: 0 16px; transition: color 0.2s, text-decoration 0.2s; cursor: pointer; }}
            nav a:hover {{ color: #3a7ca5; text-decoration: underline; }}
            h2 {{ text-align: center; color: #3a7ca5; margin-top: 32px; }}
            table {{ border-collapse: collapse; width: 90%; margin: 30px auto; background: rgba(45,45,45,0.85); border-radius: 12px; box-shadow: 0 2px 16px #222; }}
            th, td {{ border: 1px solid #3a7ca5; padding: 8px 12px; transition: background 0.2s, color 0.2s; cursor: pointer; }}
            th {{ background: #3a7ca5; color: #eaeaea; }}
            tr {{ background: #222; }}
            th:hover, td:hover {{ background: #eaeaea; color: #3a7ca5; }}
            .back {{ display: block; margin: 20px auto; background: #3a7ca5; color: #eaeaea; border: none; padding: 10px 20px; font-size: 1em; cursor: pointer; border-radius: 8px; text-align: center; width: 200px; text-decoration: none; box-shadow: 0 2px 8px #222; transition: background 0.2s, color 0.2s, box-shadow 0.2s; }}
            .back:hover {{ background: #eaeaea; color: #3a7ca5; box-shadow: 0 4px 16px #3a7ca5; }}
            .footer {{ background: #222b; color: #eaeaea; text-align: center; padding: 20px 0; position: relative; left: 0; bottom: 0; width: 100%; font-size: 1em; margin-top: 100px; }}
        </style>
    </head>
    <body>
        <header>
            <h1>Insurance Client Segmentation</h1>
        </header>
        <nav>
            <a href='landing.html'>Home</a>
            <a href='sample_customer_profiles.html'>Customer Profiles</a>
            <a href='insights.html'>Insights</a>
            <a href='about.html'>About Us</a>
        </nav>
        <a class="back" href="landing.html">&#8592; Back to Landing Page</a>
        <h2>Sample Customer Profiles</h2>
        <table>
            <tr>"""
    html_content += "".join(f"<th>{key}</th>" for key in sample_profiles[0].keys()) + "</tr>"
    for profile in sample_profiles:
        html_content += "<tr>" + "".join(f"<td>{value}</td>" for value in profile.values()) + "</tr>"
    html_content += """
        </table>
        <div class="footer">
            &copy; 2025 Old Mutual Hackathon | Powered by Data-Driven Solutions
        </div>
    </body>
    </html>
    """
    html_path.write_text(html_content, encoding="utf-8")

def create_insights_page(sample_profiles):
    background_url = "https://images.pexels.com/photos/8441854/pexels-photo-8441854.jpeg?auto=compress&cs=tinysrgb&w=1600"
    html_path = Path("insights.html")
    segments = {}
    total_income = 0
    for p in sample_profiles:
        seg = p["Use Case"]
        segments[seg] = segments.get(seg, 0) + 1
        total_income += p["Income (R)"]
    avg_income = total_income / len(sample_profiles)
    html_content = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Client Insights</title>
        <link href='https://fonts.googleapis.com/css?family=Segoe+UI:400,700&display=swap' rel='stylesheet'>
        <style>
            body {{
                background: url('{background_url}') no-repeat center center fixed;
                background-size: cover;
                color: #eaeaea;
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            header {{ background: #3a7ca5cc; color: #fff; padding: 24px 0; text-align: center; box-shadow: 0 2px 8px #222; }}
            nav {{ background: #222b; color: #eaeaea; text-align: center; padding: 12px 0; font-size: 1.1em; }}
            nav a {{ color: #eaeaea; text-decoration: none; margin: 0 16px; transition: color 0.2s, text-decoration 0.2s; cursor: pointer; }}
            nav a:hover {{ color: #3a7ca5; text-decoration: underline; }}
            .container {{ max-width: 900px; margin: 40px auto 200px auto; text-align: center; padding: 32px; background: rgba(45,45,45,0.85); border-radius: 16px; box-shadow: 0 2px 16px #222; }}
            h2 {{ color: #3a7ca5; margin-bottom: 32px; }}
            .insight-list {{ list-style: none; padding: 0; }}
            .insight-list li {{ background: #222; color: #eaeaea; margin: 16px 0; padding: 20px; border-radius: 8px; font-size: 1.2em; box-shadow: 0 2px 8px #222; transition: background 0.2s, color 0.2s; cursor: pointer; }}
            .insight-list li:hover {{ background: #3a7ca5; color: #fff; }}
            .footer {{ background: #222b; color: #eaeaea; text-align: center; padding: 20px 0; position: relative; left: 0; bottom: 0; width: 100%; font-size: 1em; margin-top: 100px; }}
        </style>
    </head>
    <body>
        <header>
            <h1>Insurance Client Segmentation</h1>
        </header>
        <nav>
            <a href='landing.html'>Home</a>
            <a href='sample_customer_profiles.html'>Customer Profiles</a>
            <a href='insights.html'>Insights</a>
            <a href='about.html'>About Us</a>
        </nav>
        <div class="container">
            <h2>Client Insights</h2>
            <ul class="insight-list">
                <li>Average Income: R {avg_income:,.2f}</li>
                {''.join([f'<li>{seg}: {count} client(s)</li>' for seg, count in segments.items()])}
            </ul>
        </div>
        <div class="footer">
            &copy; 2025 Old Mutual Hackathon | Powered by Data-Driven Solutions
        </div>
    </body>
    </html>
    """
    html_path.write_text(html_content, encoding="utf-8")

def create_about_page():
    background_url = "https://images.pexels.com/photos/8441854/pexels-photo-8441854.jpeg?auto=compress&cs=tinysrgb&w=1600"
    html_path = Path("about.html")
    html_content = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>About Us</title>
        <link href='https://fonts.googleapis.com/css?family=Segoe+UI:400,700&display=swap' rel='stylesheet'>
        <style>
            body {{
                background: url('{background_url}') no-repeat center center fixed;
                background-size: cover;
                color: #eaeaea;
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            header {{ background: #3a7ca5cc; color: #fff; padding: 24px 0; text-align: center; box-shadow: 0 2px 8px #222; }}
            nav {{ background: #222b; color: #eaeaea; text-align: center; padding: 12px 0; font-size: 1.1em; }}
            nav a {{ color: #eaeaea; text-decoration: none; margin: 0 16px; transition: color 0.2s, text-decoration 0.2s; cursor: pointer; }}
            nav a:hover {{ color: #3a7ca5; text-decoration: underline; }}
            .container {{ max-width: 900px; margin: 40px auto 200px auto; text-align: center; padding: 32px; background: rgba(45,45,45,0.85); border-radius: 16px; box-shadow: 0 2px 16px #222; }}
            h2 {{ color: #3a7ca5; margin-bottom: 32px; }}
            .details {{ font-size: 1.2em; margin-top: 24px; color: #eaeaea; }}
            .footer {{ background: #222b; color: #eaeaea; text-align: center; padding: 20px 0; position: relative; left: 0; bottom: 0; width: 100%; font-size: 1em; margin-top: 100px; }}
            .email-link {{ color: #3a7ca5; text-decoration: underline; cursor: pointer; }}
            .email-link:hover {{ color: #eaeaea; background: #3a7ca5; }}
        </style>
    </head>
    <body>
        <header>
            <h1>Insurance Client Segmentation</h1>
        </header>
        <nav>
            <a href='landing.html'>Home</a>
            <a href='sample_customer_profiles.html'>Customer Profiles</a>
            <a href='insights.html'>Insights</a>
            <a href='about.html'>About Us</a>
        </nav>
        <div class="container">
            <h2>About Us</h2>
            <div class="details">
                <p><strong>Name:</strong> Anele Dyubhele</p>
                <p><strong>Email:</strong> <a class='email-link' href='mailto:dyubheleanele@gmail.com'>dyubheleanele@gmail.com</a></p>
                <p><strong>Role:</strong> IT Trainee</p>
                <p><strong>Company:</strong> Old Mutual</p>
                <p><strong>Project:</strong> Data-Driven Client Segmentation & Targeting</p>
            </div>
        </div>
        <div class="footer">
            &copy; 2025 Old Mutual Hackathon | Powered by Data-Driven Solutions
        </div>
    </body>
    </html>
    """
    html_path.write_text(html_content, encoding="utf-8")

def open_in_chrome(html_file):
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    chrome_path = next((p for p in chrome_paths if os.path.exists(p)), None)
    if chrome_path:
        subprocess.run([chrome_path, str(html_file.resolve())], check=True)
    else:
        webbrowser.open(str(html_file.resolve()))

def main():
    sample_profiles = generate_sample_profiles()
    create_landing_page()
    create_profiles_page(sample_profiles)
    create_insights_page(sample_profiles)
    create_about_page()
    open_in_chrome(Path("landing.html"))

if __name__ == "__main__":
    main()