document.querySelector("form").onsubmit = async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  console.log(formData);
  const response = await fetch("/generate", {
    method: "POST",
    body: formData,
  });
  console.log(response);
  const result = await response.json();
  document.getElementById("output").innerText = result.recipe || result.error;
};
