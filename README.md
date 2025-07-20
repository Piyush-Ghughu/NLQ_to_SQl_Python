<div align="center"
  style="background: linear-gradient(to right, #667eea, #764ba2); padding: 30px; border-radius: 10px; color: white;">
  <h1 style="font-size: 2.5rem; margin-bottom: 10px;">🤖 LLM-Powered Chatbot</h1>
  <h3 style="font-weight: normal;">FastAPI + React + MySQL + Groq LLMs</h3>
</div>
<hr>
<div align="center" style="margin-bottom: 20px;">
  <h2 style="color:#ff6f61;">🎥 Live Demo</h2>
  <video width="80%" controls>
    <source src="assets/video1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p style="font-style: italic; color: #888;">Watch the chatbot convert your natural language queries to real-time SQL
    and display database results instantly.</p>
</div>

<h2 style="color:#764ba2;">🛠️ How This Project Was Built</h2>

<ul>
  <li><span style="color:#333;"><strong>Frontend:</strong> React (HTML + CSS + Axios)</span></li>
  <li><span style="color:#333;"><strong>Backend:</strong> FastAPI with REST endpoints</span></li>
  <li><span style="color:#333;"><strong>LLM:</strong> Groq-hosted LLaMA or Mistral for converting natural language to
      SQL</span></li>
  <li><span style="color:#333;"><strong>Database:</strong> MySQL with a <code>customer</code> table</span></li>
  <li><span style="color:#333;"><strong>Security:</strong> API Key stored securely in <code>.env</code> file</span></li>
</ul>

<hr>

<h2 style="color:#764ba2;">🚀 Getting Started</h2>

<ol>
  <li><b>Install React dependencies:</b><br><code>cd frontpart</code><br><code>npm install</code></li>
  <li><b>Build the React frontend:</b><br><code>npm run build</code></li>
  <li><b>Return to backend:</b><br><code>cd ..</code></li>
  <li><b>Create .env file:</b><br><code>echo "GROQ_API_KEY=your_key_here" > .env</code></li>
  <li><b>Install Python backend
      packages:</b><br><code>pip install fastapi uvicorn python-dotenv requests mysql-connector-python</code></li>
  <li><b>Run the FastAPI server:</b><br><code>.\venv\Scripts\activate</code><br><code>uvicorn main:app --reload</code>
  </li>
</ol>

<hr>

<h2 style="color:#764ba2;">🌐 Access the App</h2>

<ul>
  <li><b>Frontend:</b> <a href="http://localhost:3000" target="_blank">http://localhost:3000</a></li>
  <li><b>API Endpoint:</b> <code>POST /query</code></li>
</ul>

<hr>

<h2 style="color:#764ba2;">🧪 Try These Sample Questions</h2>

<ul>
  <li>Who lives in Mumbai?</li>
  <li>Show all customers</li>
  <li>Get names and phone numbers from Delhi</li>
  <li>List all female customers</li>
</ul>

<hr>

<h2 style="color:#764ba2;">📦 Tech Stack Used</h2>

<table style="width:100%; border:1px solid #ddd;">
  <tr style="background:#f6f6f6;">
    <th align="left">Layer</th>
    <th align="left">Technology</th>
  </tr>
  <tr>
    <td>💡 LLM</td>
    <td>Groq-hosted LLaMA or Mistral</td>
  </tr>
  <tr>
    <td>🎨 Frontend</td>
    <td>HTML, CSS, ReactJS</td>
  </tr>
  <tr>
    <td>🧠 Backend</td>
    <td>Python, FastAPI</td>
  </tr>
  <tr>
    <td>🗄️ Database</td>
    <td>MySQL</td>
  </tr>
  <tr>
    <td>🔐 Secrets</td>
    <td>.env</td>
  </tr>
</table>

<hr>

<h2 style="color:#764ba2;">🔐 Security Notes</h2>

<ul>
  <li>✅ API key is hidden using <code>.env</code></li>
  <li>✅ <code>.env</code> is ignored in git with <code>.gitignore</code></li>
  <li>✅ Only SELECT queries allowed from LLM</li>
</ul>

<hr>

<h2 style="color:#764ba2; text-align:center;">📸 Screenshots</h2>

<div style="text-align:center;">
  <h3 style="color:#4caf50;">✅ Successfully Executed Query</h3>
  <img src="assets/1.png" alt="Chat UI" width="600" style="border:1px solid #ccc; border-radius:10px;" />
  <p style="color:#555; font-size:16px;">The chatbot successfully converted a natural language query into SQL and
    displayed the result from the database.</p>
</div>

<br />

<div style="text-align:center;">
  <h3 style="color:#f44336;">❌ Unrecognized Query</h3>
  <img src="assets/2.png" alt="SQL Table" width="600" style="border:1px solid #ccc; border-radius:10px;" />
  <p style="color:#555; font-size:16px;">When the chatbot cannot interpret the natural language input, it responds with
    a fallback message prompting for a clearer query.</p>
</div>


<hr>

<h2 style="color:#764ba2;">📌 Future Enhancements</h2>

<ul>
  <li>🔐 Add authentication system</li>
  <li>📡 Deploy backend to cloud (Render/Railway)</li>
  <li>🗃️ Add support for more tables and databases</li>
  <li>📤 Add file upload to import customer data</li>
</ul>

<hr>

<h2 style="color:#764ba2;">🤝 Contributing</h2>
<p>If you like this project, feel free to fork it and raise PRs for suggestions!</p>