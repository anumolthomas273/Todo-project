document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const passwordField = document.querySelector('input[type="password"]');
    const toggleBtn = document.createElement("span");
    const submitBtn = form.querySelector("button[type='submit']");

    // Add show/hide toggle
    toggleBtn.innerText = "👁️";
    toggleBtn.style.cursor = "pointer";
    toggleBtn.style.position = "absolute";
    toggleBtn.style.right = "10px";
    toggleBtn.style.top = "36px";
    toggleBtn.title = "Show/Hide Password";

    const passwordWrapper = passwordField.parentElement;
    passwordWrapper.style.position = "relative";
    passwordWrapper.appendChild(toggleBtn);

    toggleBtn.addEventListener("click", () => {
        if (passwordField.type === "password") {
            passwordField.type = "text";
            toggleBtn.innerText = "🙈";
        } else {
            passwordField.type = "password";
            toggleBtn.innerText = "👁️";
        }
    });

    // Disable submit button if required fields are empty
    function validateForm() {
        const inputs = form.querySelectorAll("input[required]");
        let isValid = true;
        inputs.forEach((input) => {
            if (input.value.trim() === "") {
                isValid = false;
            }
        });
        submitBtn.disabled = !isValid;
        submitBtn.style.opacity = isValid ? "1" : "0.6";
    }

    // Add input listeners
    form.querySelectorAll("input[required]").forEach((input) => {
        input.addEventListener("input", validateForm);
    });

    // Initial validation
    validateForm();
});
