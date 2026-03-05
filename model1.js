const response = await fetch(
  "https://cors-anywhere.herokuapp.com/https://doctor-finding.onrender.com/predict",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      symptoms: symptoms,
      address: address
    })
  }
);
