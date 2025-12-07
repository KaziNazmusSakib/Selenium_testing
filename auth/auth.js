// Save user to LocalStorage
function saveUser(user) {
    localStorage.setItem("user", JSON.stringify(user));
}

// Get user from LocalStorage
function getUser() {
    return JSON.parse(localStorage.getItem("user"));
}

/* Signin Handler */

const signupForm = document.getElementById("signupForm");

if(signupForm) {
    signupForm.addEventListener("submit", (e) => {
        e.preventDefault();
        
        let username = document.getElementById("signupUser").value.trim();
        let email = document.getElementById("signupEmail").value.trim();
        let password = document.getElementById("signupPassword").value.trim();

        if(!username || !email || !password) {
            alert("All fields are required!");
            return;
        }

        const user = { username, email, password };
        saveUser(user);

        alert("Account created successfully!");
        window.location.href = "/auth/login.html"
        //<a href="/auth/login.html">Login</a>
    });
}

/* Login Handler */

const loginForm = document.getElementById("loginForm");


if(loginForm) {
    loginForm.addEventListener("submit", (e) => {
        e.preventDefault();

        let email = document.getElementById("loginEmail").value.trim();
        let password = document.getElementById("loginPassword").value.trim();
        
        const user = getUser();
        
        if(!user) {
            alert("No user found! Please sign up first.");
            return;
        } 

        if(user.email === email && user.password === password) {
            alert("Login  successfull.");
            window.location.href = "/index.html";
        } else {
            alert("Invalid email or password");
        } 
    });
}
