import './card.css'


export default function Card({ card, title, description, image, setRecommendations }) {

  const clickButton = async (itemData) => {

  const recIndex =
  itemData.id
    .split("")
    .reduce((acc, char) => acc + char.charCodeAt(0), 0) % 3000;


  try {
    const response = await fetch(
      "http://127.0.0.1:5000/recommend",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
        image: itemData.urls.regular
        }),
      }
    );

    const result = await response.json();
    console.log("AI Recommendations:", result);

    // We will display this next
    setRecommendations(result);
    console.log(result);

  } catch (error) {
    console.error("Error fetching recommendations:", error);
  }
};



  return (
    <div className="card" >
      <img className="card-image" src={image} alt={title} />

      <div className="card-content">
        <h3 className="card-title">{title}</h3>
        <p className="card-description">{description}</p>

        <button className="card-button" onClick={()=>clickButton(card)}>Learn More</button>

      </div>
    </div>
  );
}
