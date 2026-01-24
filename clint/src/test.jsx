import React, { useState, useEffect } from 'react';

const ConnectionTest = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const testBackend = async () => {
    try {
      // Replace with your actual Flask URL
      const response = await fetch('https://stunning-succotash-pj966456x9rx26rw4-5000.app.github.dev/reconnect');
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      
      const result = await response.json();
      setData(result);
    } catch (e) {
      setError(e.message);
      console.error("Connection error:", e);
    }
  };

  return (
    <div style={{ padding: '20px', border: '2px solid #61dafb', margin: '20px', borderRadius: '8px' }}>
      <h3>Backend Connection Test</h3>
      <button onClick={testBackend}>Click to Ping Flask</button>
      
      {data && <p style={{ color: 'green' }}>✅ Success: {JSON.stringify(data)}</p>}
      {error && <p style={{ color: 'red' }}>❌ Error: {error}</p>}
    </div>
  );
};

export default ConnectionTest;