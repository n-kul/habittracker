const form = document.getElementById("habit-form");
const progressDiv = document.getElementById("progress");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const gym = document.getElementById("gym").checked;
  const study = document.getElementById("study").checked;
  const wake = document.getElementById("wake").checked;

  const res = await fetch("https://YOUR-BACKEND-URL/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, gym, study, wake })
  });

  await loadProgress();
});

async function loadProgress() {
  const res = await fetch("https://YOUR-BACKEND-URL/progress");
  const data = await res.json();
  progressDiv.innerHTML = "";

  data.progress.forEach(([user, gym, study, wake]) => {
    const status = `
      <strong>${user}</strong>: 
      Gym: ${gym ? "✅" : "❌"}, 
      Study: ${study ? "✅" : "❌"}, 
      Wake Early: ${wake ? "✅" : "❌"}
    `;
    const p = document.createElement("p");
    p.innerHTML = status;
    progressDiv.appendChild(p);
  });
}

// Load on start
loadProgress();
