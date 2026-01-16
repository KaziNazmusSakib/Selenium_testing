// Save user to LocalStorage
function saveUser(user) {
    localStorage.setItem("user", JSON.stringify(user));
}

// Get user from LocalStorage
function getUser() {
    return JSON.parse(localStorage.getItem("user"));
}

 
/* ================= SIGN UP ================= */

const signupForm = document.getElementById("signupForm");

if (signupForm) {
    signupForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = document.getElementById("signupUser").value.trim();
        const email = document.getElementById("signupEmail").value.trim();
        const password = document.getElementById("signupPassword").value.trim();

        if (!username || !email || !password) {
            alert("All fields are required!");
            return;
        }

        const user = { username, email, password };
        saveUser(user);

        alert("Account created successfully!");
        window.location.href = "login.html";
    });
}

/* ================= LOGIN ================= */

const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const email = document.getElementById("loginEmail").value.trim();
        const password = document.getElementById("loginPassword").value.trim();

        const user = getUser();

        if (!user) {
            alert("No account found. Please sign up first.");
            return;
        }

        if (user.email === email && user.password === password) {
            alert("Login successful!");
            window.location.href = "/index.html";
        } else {
            alert("Invalid email or password");
        }
    });
}
