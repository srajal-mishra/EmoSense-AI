import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [emotion, setEmotion] = useState("Scanning...");

  // This simple timer asks Python for the latest emotion every second
  useEffect(() => {
    const timer = setInterval(() => {
      fetch('http://127.0.0.1:5000/emotion')
        .then(response => response.json())
        .then(data => {
          setEmotion(data.emotion);
        })
        .catch(err => console.log("Waiting for AI..."));
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  return (
    <div className="dashboard">
      <h1>EmoSense Dashboard</h1>
      
      <div className="video-container">
        {/* Video Feed */}
        <img 
          src="http://127.0.0.1:5000/" 
          alt="AI Video Feed" 
          className="video-feed"
        />
      </div>

      {/* Live Data Card */}
      <div className="stats-card">
        <h2>Current Student Emotion</h2>
        {/* This text changes automatically based on the AI */}
        <p className="emotion-text" style={{ color: emotion === 'fear' ? 'red' : '#00d8ff' }}>
          {emotion.toUpperCase()}
        </p>
      </div>
    </div>
  );
}

export default App;