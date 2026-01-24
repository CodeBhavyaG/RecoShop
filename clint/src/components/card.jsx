import './card.css'

export default function Card({ card ,title, description, image }) {

  const clickButton = async (itemData) => {
  try {
    const response = await fetch("https://stunning-succotash-pj966456x9rx26rw4-5000.app.github.dev/handle-click", {
      method: "POST", // 1. Use POST to send data
      headers: {
        "Content-Type": "application/json", // 2. Tell Flask to expect JSON
      },
      body: JSON.stringify({ 
        id: itemData.id, 
        title: itemData.user 
      }), // 3. Turn your JS object into a string
    });

    const result = await response.json();
    console.log("Response from Flask:", result);
  } catch (error) {
    console.error("Error sending data:", error);
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
