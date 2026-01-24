
import './App.css'
import Card from './components/card.jsx'
import { useEffect,useState } from 'react';

function App() {
  const [arr,setarr]=useState([])
  useEffect(()=>{
    fetch("https://stunning-succotash-pj966456x9rx26rw4-5000.app.github.dev/reconnect")
    .then(res=>res.json())
    .then(data=>setarr(data.hits))
    .catch(error=>console.error(error)
    )
  },[])


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
            {arr.map((card) => (
              <Card
                key={card.id}
                card={card}
                title={card.user}
                description={card.tags}
                image={card.largeImageURL}
              />
            ))}
          </div>
        </main>

      </div>
    </div>
  );
}


export default App;
