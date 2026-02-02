import './App.css'
import Card from './components/card.jsx'
import { useEffect,useState } from 'react';

function App() {
  const [arr,setArr]=useState([])
  const [recommendations, setRecommendations] = useState([]);


  useEffect(() => {
  fetch("http://127.0.0.1:5000/reconnect")
    .then(res => res.json())
    .then(data => { 
      console.log("Unsplash response:", data);
      setArr(data.results || []);
})
    .catch(err => console.error(err));
}, []);


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
            {Array.isArray(arr) && arr.map((card) => (

              <Card
                key={card.id}
                card={card}
                title={card.user.name}
                description={card.alt_description || "No description"}
                image={card.urls.regular}
                setRecommendations={setRecommendations}
              />



            ))}
          </div>
          {recommendations.length > 0 && (
          <>
            <h2 style={{ marginTop: "40px" }}>Recommended for you</h2>

            <div className="card-container">
              {recommendations.map((rec, index) => (
                <div className="card" key={index}>
                  <img
                    className="card-image"
                    src={rec.image}
                    alt={rec.title}
                  />
                  <div className="card-content">
                    <p className="card-description">
                      {rec.title}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}


        </main>

      </div>
    </div>
  );
}


export default App;
