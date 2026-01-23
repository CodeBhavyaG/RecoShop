import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card from './components/card.jsx'

function App() {
  const cardData = Array.from({ length: 10 }, (_, index) => ({
    id: index,
    title: `Card Title ${index + 1}`,
    description: "This is a reusable React card component.",
    image: "https://picsum.photos/300/200"
  }));

  return (
    <div className="app">

      {/* TOP SECTION */}
      <header className="topbar">
        <h2>RecoShop</h2>
      </header>

      {/* BODY SECTION */}
      <div className="body">

        {/* LEFT PART */}
        <aside className="sidebar">
          <ul>
            <li>Dashboard</li>
            <li>Products</li>
            <li>Orders</li>
            <li>Profile</li>
          </ul>
        </aside>

        {/* MIDDLE PART */}
        <main className="content">
          <div className="card-container">
            {cardData.map((card) => (
              <Card
                key={card.id}
                title={card.title}
                description={card.description}
                image={card.image}
              />
            ))}
          </div>
        </main>

      </div>
    </div>
  );
}

export default App;
