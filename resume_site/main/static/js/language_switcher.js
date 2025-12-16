document.addEventListener('DOMContentLoaded', function() {
    // Функція, яка визначає, яка мова має бути активною, і перемикає клас.
    function updateActiveLanguage() {
        const urlParams = new URLSearchParams(window.location.search);
        // Беремо параметр ?lang=... з URL.
        let currentLang = urlParams.get('lang'); 

        // Якщо параметр lang не встановлено, встановлюємо мову за замовчуванням (UA)
        if (!currentLang) {
            currentLang = 'ua';
        }

        // 1. Видаляємо клас 'active' з усіх прапорців
        // Ми вибираємо всі картинки, які є прямими нащадками .language-switcher
        const allFlags = document.querySelectorAll('.language-switcher img');
        allFlags.forEach(img => img.classList.remove('active'));

        // 2. Додаємо клас 'active' до потрібного прапорця
        // Знаходимо посилання (<a>) за ID, який ми встановили в HTML
        const activeLinkElement = document.getElementById(`lang-${currentLang}`);

        if (activeLinkElement) {
            // Клас active має бути на самій картинці (<img>) всередині посилання
            const imgElement = activeLinkElement.querySelector('img');
            if (imgElement) {
                imgElement.classList.add('active');
            }
        }
    }

    // Викликаємо функцію, коли DOM повністю завантажився
    updateActiveLanguage();
});