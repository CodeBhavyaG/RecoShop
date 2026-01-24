
import './App.css'
import Card from './components/card.jsx'
import ConnectionTest from './test.jsx'

/*function App() {
  const cardData = Array.from({ length: 10 }, (_, index) => ({
    id: index,
    title: `Card Title ${index + 1}`,
    description: "This is a reusable React card component.",
    image: "https://picsum.photos/300/200"
  }));

  return (
    <div className="app">

      
      <header className="topbar">
        <h2>RecoShop</h2>
      </header>

      
      <div className="body">

       
        <aside className="sidebar">
          <ul>
            <li>Dashboard</li>
            <li>Products</li>
            <li>Orders</li>
            <li>Profile</li>
          </ul>
        </aside>

        
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
*/


function App() {
  return (
    <div className="App">
      {/* This is your safety sandbox */}
      <ConnectionTest /> 

      <hr />
      
      {/* Your main app content stays here, untouched */}
      <header>
        <h1>My Main App Content</h1>
      </header>
    </div>
  );
}

export default App;
