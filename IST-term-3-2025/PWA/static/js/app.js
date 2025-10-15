document.addEventListener("DOMContentLoaded", () => {
  // -----------------------------
  // Complete checkbox (tasks)
  // -----------------------------
  document.querySelectorAll(".complete-checkbox").forEach((checkbox) => {
    checkbox.addEventListener("change", (e) => {
      const li = e.target.closest("li");
      const id = li.dataset.id;

      fetch(`/complete/${id}`, { method: "POST" }).then(() => {
        li.querySelector("span").classList.toggle("completed");
      });
    });
  });

  // -----------------------------
  // Delete button (tasks)
  // -----------------------------
  document.querySelectorAll(".delete-btn").forEach((button) => {
    button.addEventListener("click", (e) => {
      const li = e.target.closest("li");
      const id = li.dataset.id;

      fetch(`/delete/${id}`, { method: "POST" }).then(() => li.remove());
    });
  });

  // -----------------------------
  // Delete button (lists)
  // -----------------------------
  function deleteList(id) {
    fetch(`/delete_list/${id}`, { method: "POST" })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          const listCard = document.getElementById(`list-${id}`);
          listCard.style.transition = "opacity 0.4s ease";
          listCard.style.opacity = 0;
          setTimeout(() => listCard.remove(), 400);
        } else {
          console.error("Failed to delete list:", data.error);
        }
      })
      .catch(err => console.error("Error deleting list:", err));
  }

  // Attach deleteList to all list delete buttons
  document.querySelectorAll(".delete-list-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.dataset.id;
      deleteList(id);
    });
  });

  // Optional: make deleteList global if you need it elsewhere
  window.deleteList = deleteList;
});
