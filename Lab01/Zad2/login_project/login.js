const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();

    // Definicja z wyciągnięciem wartości username i password z formularza
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // Walidacja pól username i password w formularzu
    if (username === "" && password === "") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
