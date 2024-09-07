// Sidebar pin-drops
(function() {
    const pinTitle = document.querySelector(".pin-title");
    let pinIcon = document.querySelectorAll(".sidebar-list .fa-thumb-tack");

    function togglePinnedName() {
        if (document.getElementsByClassName("pined").length) {
            if (!pinTitle.classList.contains("show")) pinTitle.classList.add("show");
        } else {
            pinTitle.classList.remove("show");
        }
    }

    pinIcon.forEach((item, index) => {
        var linkName = item.parentNode.querySelector("span").innerHTML;
        var InitialLocalStorage = JSON.parse(localStorage.getItem("pins") || false);

        if (InitialLocalStorage && InitialLocalStorage.includes(linkName)) {
            item.parentNode.classList.add("pined");
        }
        item.addEventListener("click", (event) => {
            var localStoragePins = JSON.parse(localStorage.getItem("pins") || false);
            item.parentNode.classList.toggle("pined");

            if (localStoragePins ? .length) {
                if (item.parentNode.classList.contains("pined")) {
                    !localStoragePins ? .includes(linkName) &&
                        (localStoragePins = [...localStoragePins, linkName]);
                } else {
                    localStoragePins ? .includes(linkName) &&
                        localStoragePins.splice(localStoragePins.indexOf(linkName), 1);
                }
                localStorage.setItem("pins", JSON.stringify(localStoragePins));
            } else {
                localStorage.setItem("pins", JSON.stringify([linkName]));
            }

            var elem = item;
            var topPos = elem.offsetTop;
            togglePinnedName();
            if (item.parentElement.parentElement.classList.contains("pined")) {
                scrollTo(
                    document.getElementsByClassName("simplebar-content-wrapper")[0],
                    topPos - 30,
                    600
                );
            } else {
                scrollTo(
                    document.getElementsByClassName("simplebar-content-wrapper")[0],
                    elem.parentNode.offsetTop - 30,
                    600
                );
            }
        });

        function scrollTo(element, to, duration) {
            var start = element.scrollTop,
                change = to - start,
                currentTime = 0,
                increment = 20;

            var animateScroll = function() {
                currentTime += increment;
                var val = Math.easeInOutQuad(currentTime, start, change, duration);
                element.scrollTop = val;
                if (currentTime < duration) {
                    setTimeout(animateScroll, increment);
                }
            };
            animateScroll();
        }

        Math.easeInOutQuad = function(t, b, c, d) {
            t /= d / 2;
            if (t < 1) return (c / 2) * t * t + b;
            t--;
            return (-c / 2) * (t * (t - 2) - 1) + b;
        };
    });
    togglePinnedName();
})();