
import './App.css'
import Card from './components/card.jsx'
import { useEffect,usestate } from 'react';

function App() {
  const [Arr,setarr]=usestate([{}])
  useEffect(()=>{
    fetch("https://potential-space-waffle-jjgp9xj5pvqrhp7vq-5000.app.github.dev/reconnect")
    .then(res=>res.json())
    .then(data=>setarr(data))
    .catch(error=>console.error(error)
    )
  })
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


export default App;
