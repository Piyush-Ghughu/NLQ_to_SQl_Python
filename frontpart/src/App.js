import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [chatLog, setChatLog] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleQuery = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    const userMessage = { role: 'user', content: query };
    setChatLog((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });

      const data = await response.json();
      let resultText = '';

      // ✅ Handle message-only responses (like greetings or fallback)
      if (data.message) {
        resultText = data.message;
      }
      // ✅ Handle errors
      else if (data.error) {
        resultText = '❌ Error: ' + data.error;
      }
      // ✅ Handle valid SQL result
      else if (data.result && data.result.length > 0) {
        resultText = `🧠 Results for "${query}":\n\n`;
        resultText += data.result
          .map((row, i) => {
            let line = `${i + 1}. ${row.name}`;
            if (row.ph_number) line += ` — ${row.ph_number}`;
            if (row.location) line += ` (${row.location})`;
            return line;
          })
          .join('\n');
      } else {
        resultText = '❌ No results found.';
      }

      const botMessage = {
        role: 'bot',
        content: resultText
      };

      setChatLog((prev) => [...prev, botMessage]);
    } catch (error) {
      setChatLog((prev) => [
        ...prev,
        { role: 'bot', content: '❌ Error talking to backend.' }
      ]);
    }

    setQuery('');
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h2>💬 Piyush Chat Application</h2>

      <div className="chat-box">
        {chatLog.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <pre>{msg.content}</pre>
          </div>
        ))}
        {loading && <div className="message bot">🤔 Thinking...</div>}
      </div>

      <form className="input-form" onSubmit={handleQuery}>
        <input
          type="text"
          placeholder="Ask something like: who lives in Mumbai?"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
