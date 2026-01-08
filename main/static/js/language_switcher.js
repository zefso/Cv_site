document.addEventListener('DOMContentLoaded', function() {
    function updateActiveLanguage() {
        const urlParams = new URLSearchParams(window.location.search);
        let currentLang = urlParams.get('lang'); 


        if (!currentLang) {
            currentLang = 'ua';
        }


        const allFlags = document.querySelectorAll('.language-switcher img');
        allFlags.forEach(img => img.classList.remove('active'));

        const activeLinkElement = document.getElementById(`lang-${currentLang}`);

        if (activeLinkElement) {
            const imgElement = activeLinkElement.querySelector('img');
            if (imgElement) {
                imgElement.classList.add('active');
            }
        }
    }
    updateActiveLanguage();
});