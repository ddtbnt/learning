function addRecommendation() {
  let message = document.getElementById("new_recommendation_text");
  
  if (message.value != null && message.value.trim() != "") {
    // Logic thêm nhận xét cũ của anh
    var element = document.createElement("div");
    element.setAttribute("class", "recommendation-card");
    element.innerHTML = "<p>\"" + message.value + "\"</p><cite>- Anonymous Visitor</cite>";
    document.getElementById("all_recommendations").appendChild(element);
    
    // --- PHẦN CHO TASK 9 ---
    // Hiển thị thông báo Pop-up
    alert("Thank you for leaving a recommendation!");
    // -----------------------

    message.value = "";
  }
}