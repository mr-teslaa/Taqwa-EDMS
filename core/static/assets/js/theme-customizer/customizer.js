(function($) {
    if (localStorage.getItem("color"))
        $("#color").attr(
            "href",
            "../assets/css/" + localStorage.getItem("color") + ".css"
        );
    if (localStorage.getItem("dark")) $("body").attr("class", "dark-only");
    $(
        '<div class="customizer-links"><div class="nav flex-column nac-pills" id="c-pills-tab" role="tablist" aria-orientation="vertical"><a class="nav-link" id="c-pills-layouts-tab" data-bs-toggle="pill" href="#c-pills-layouts" role="tab" aria-controls="c-pills-layouts" aria-selected="true" data-original-title=""><span>Check layouts</span></a> <a class="nav-link" id="c-pills-home-tab" data-bs-toggle="pill" href="#c-pills-home" role="tab" aria-controls="c-pills-home" aria-selected="true" data-original-title=""><div class="settings"><img src="../assets/images/customizer/color.png" alt=""></div><span>Quick option</span></a> <a class="nav-link" target="_blank" href="https://support.pixelstrap.com/" data-original-title=""><div><img src="../assets/images/customizer/support.png" alt=""></div><span>Support</span></a> <a class="nav-link" target="_blank" href="https://docs.pixelstrap.net/mofi/document/" target="_blank" data-original-title=""><div><img src="../assets/images/customizer/setting.png" alt=""></div><span>Document</span></a> <a class="nav-link" target="_blank" href="https://admin.pixelstrap.net/mofi/template/landing-page.html" data-original-title=""><div><img src="../assets/images/customizer/features.png" alt=""></div><span>Check features</span></a> <a class="nav-link" target="_blank" href="https://themeforest.net/user/pixelstrap/portfolio" data-original-title=""><div><img src="../assets/images/customizer/document.png" alt=""></div><span>Buy now</span></a></div></div><div class="customizer-contain"><div class="tab-content" id="c-pills-tabContent"><div class="customizer-header"><i class="icofont-close icon-close"></i><h5 class="f-w-700">Preview Settings</h5><p class="mb-0">Try It Real Time <i class="fa fa-thumbs-o-up txt-primary"></i></p></div><div class="customizer-body custom-scrollbar"><div class="tab-pane fade show active" id="c-pills-home" role="tabpanel" aria-labelledby="c-pills-home-tab"><h5>Layout Type</h5><ul class="main-layout layout-grid"><li data-attr="ltr" class="active"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body"><ul><li class="bg-light sidebar"></li><li class="bg-light body"><span class="badge badge-primary">LTR</span></li></ul></div></li><li data-attr="rtl"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body"><ul><li class="bg-light body me-1"><span class="badge badge-primary">RTL</span></li><li class="bg-light sidebar"></li></ul></div></li><li data-attr="ltr" class="box-layout px-3"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body"><ul><li class="bg-light sidebar"></li><li class="bg-light body"><span class="badge badge-primary">Box</span></li></ul></div></li></ul><h5>Sidebar Type</h5><ul class="sidebar-type layout-grid"><li data-attr="normal-sidebar"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body"><ul><li class="bg-dark sidebar"></li><li class="bg-light body"></li></ul></div></li><li data-attr="compact-sidebar"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body"><ul><li class="bg-dark sidebar compact"></li><li class="bg-light body"></li></ul></div></li></ul><h5>Sidebar Icon</h5><ul class="sidebar-setting layout-grid"><li class="active" data-attr="stroke-svg"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body bg-light"><span class="badge badge-primary">Stroke</span></div></li><li data-attr="fill-svg"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body bg-light"><span class="badge badge-primary">Fill</span></div></li></ul><h5>Unlimited Color</h5><ul class="layout-grid unlimited-color-layout"><input id="ColorPicker1" type="color" value="#7A70BA" name="Background"><input id="ColorPicker2" type="color" value="#48A3D7" name="Background"><button type="button" class="color-apply-btn btn btn-primary color-apply-btn">Apply</button></ul><h5>Light layout</h5><ul class="layout-grid customizer-color"><li class="color-layout" data-attr="color-1" data-primary="#7A70BA" data-secondary="#48A3D7"><div></div></li><li class="color-layout" data-attr="color-2" data-primary="#88967e" data-secondary="#29353a"><div></div></li><li class="color-layout" data-attr="color-3" data-primary="#c6164f" data-secondary="#372363"><div></div></li><li class="color-layout" data-attr="color-4" data-primary="#4b232d" data-secondary="#8e6343"><div></div></li><li class="color-layout" data-attr="color-5" data-primary="#007a91" data-secondary="#534686"><div></div></li><li class="color-layout" data-attr="color-6" data-primary="#56409f" data-secondary="#21637f"><div></div></li></ul><h5>Dark Layout</h5><ul class="layout-grid customizer-color dark"><li class="color-layout" data-attr="color-1" data-primary="#7A70BA" data-secondary="#48A3D7"><div></div></li><li class="color-layout" data-attr="color-2" data-primary="#88967e" data-secondary="#29353a"><div></div></li><li class="color-layout" data-attr="color-3" data-primary="#c6164f" data-secondary="#372363"><div></div></li><li class="color-layout" data-attr="color-4" data-primary="#4b232d" data-secondary="#8e6343"><div></div></li><li class="color-layout" data-attr="color-5" data-primary="#007a91" data-secondary="#534686"><div></div></li><li class="color-layout" data-attr="color-6" data-primary="#56409f" data-secondary="#21637f"><div></div></li></ul><h5>Mix Layout</h5><ul class="layout-grid customizer-mix"><li class="color-layout" data-attr="dark-sidebar"><div class="header bg-light"><ul><li></li><li></li><li></li></ul></div><div class="body"><ul><li class="bg-dark sidebar"></li><li class="bg-light body"></li></ul></div></li><li class="color-layout" data-attr="dark-only"><div class="header bg-dark"><ul><li></li><li></li><li></li></ul></div><div class="body"><ul><li class="bg-dark sidebar"></li><li class="bg-dark body"></li></ul></div></li></ul></div><div class="tab-pane fade" id="c-pills-layouts" role="tabpanel" aria-labelledby="c-pills-layouts-tab"></div></div></div></div>'
    ).appendTo($("body"));
    (function() {})();
    //live customizer js
    $(document).ready(function() {
        $(".customizer-color li").on("click", function() {
            $(".customizer-color li").removeClass("active");
            $(this).addClass("active");
            var color = $(this).attr("data-attr");
            var primary = $(this).attr("data-primary");
            var secondary = $(this).attr("data-secondary");
            localStorage.setItem("color", color);
            localStorage.setItem("primary", primary);
            localStorage.setItem("secondary", secondary);
            localStorage.removeItem("dark");
            $("#color").attr("href", "../assets/css/" + color + ".css");
            $(".dark-only").removeClass("dark-only");
            location.reload(true);
        });

        $(".customizer-color.dark li").on("click", function() {
            $(".customizer-color.dark li").removeClass("active");
            $(this).addClass("active");
            $("body").attr("class", "dark-only");
            localStorage.setItem("dark", "dark-only");
        });

        if (localStorage.getItem("primary") != null) {
            document.documentElement.style.setProperty(
                "--theme-default",
                localStorage.getItem("primary")
            );
        }
        if (localStorage.getItem("secondary") != null) {
            document.documentElement.style.setProperty(
                "--theme-secondary",
                localStorage.getItem("secondary")
            );
        }
        $(
            ".customizer-links #c-pills-home-tab, .customizer-links #c-pills-layouts-tab"
        ).click(function() {
            $(".customizer-contain").addClass("open");
            $(".customizer-links").addClass("open");
        });

        $(".close-customizer-btn").on("click", function() {
            $(".floated-customizer-panel").removeClass("active");
        });

        $(".customizer-contain .icon-close").on("click", function() {
            $(".customizer-contain").removeClass("open");
            $(".customizer-links").removeClass("open");
        });

        $(".color-apply-btn").click(function() {
            location.reload(true);
        });

        var primary = document.getElementById("ColorPicker1").value;
        document.getElementById("ColorPicker1").onchange = function() {
            primary = this.value;
            localStorage.setItem("primary", primary);
            document.documentElement.style.setProperty("--theme-primary", primary);
        };

        var secondary = document.getElementById("ColorPicker2").value;
        document.getElementById("ColorPicker2").onchange = function() {
            secondary = this.value;
            localStorage.setItem("secondary", secondary);
            document.documentElement.style.setProperty(
                "--theme-secondary",
                secondary
            );
        };

        $(".customizer-color.dark li").on("click", function() {
            $(".customizer-color.dark li").removeClass("active");
            $(this).addClass("active");
            $("body").attr("class", "dark-only");
            localStorage.setItem("dark", "dark-only");
        });

        $(".customizer-mix li").on("click", function() {
            $(".customizer-mix li").removeClass("active");
            $(this).addClass("active");
            var mixLayout = $(this).attr("data-attr");
            $("body").attr("class", mixLayout);
        });

        $(".sidebar-setting li").on("click", function() {
            $(".sidebar-setting li").removeClass("active");
            $(this).addClass("active");
            var sidebar = $(this).attr("data-attr");
            $(".sidebar-wrapper").attr("data-layout", sidebar);
        });

        $(".sidebar-main-bg-setting li").on("click", function() {
            $(".sidebar-main-bg-setting li").removeClass("active");
            $(this).addClass("active");
            var bg = $(this).attr("data-attr");
            $(".sidebar-wrapper").attr("class", "sidebar-wrapper " + bg);
        });

        $(".sidebar-type li").on("click", function() {
            $("body").append("");
            console.log("test");
            var type = $(this).attr("data-attr");

            var boxed = "";
            if ($(".page-wrapper").hasClass("box-layout")) {
                boxed = "box-layout";
            }
            switch (type) {
                case "compact-sidebar":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-wrapper " + boxed
                        );
                        $(this).addClass("active");
                        localStorage.setItem("page-wrapper", "compact-wrapper");
                        break;
                    }
                case "normal-sidebar":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper horizontal-wrapper " + boxed
                        );
                        $(".logo-wrapper")
                        .find("img")
                        .attr("src", "../assets/images/logo/logo.png");
                        localStorage.setItem("page-wrapper", "horizontal-wrapper");
                        break;
                    }
                case "default-body":
                    {
                        $(".page-wrapper").attr("class", "page-wrapper  only-body" + boxed);
                        localStorage.setItem("page-wrapper", "only-body");
                        break;
                    }
                case "dark-sidebar":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-wrapper dark-sidebar" + boxed
                        );
                        localStorage.setItem("page-wrapper", "compact-wrapper dark-sidebar");
                        break;
                    }
                case "compact-wrap":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-sidebar" + boxed
                        );
                        localStorage.setItem("page-wrapper", "compact-sidebar");
                        break;
                    }
                case "color-sidebar":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-wrapper color-sidebar" + boxed
                        );
                        localStorage.setItem("page-wrapper", "compact-wrapper color-sidebar");
                        break;
                    }
                case "compact-small":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-sidebar compact-small" + boxed
                        );
                        localStorage.setItem("page-wrapper", "compact-sidebar compact-small");
                        break;
                    }
                case "box-layout":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-wrapper box-layout " + boxed
                        );
                        localStorage.setItem("page-wrapper", "compact-wrapper box-layout");
                        break;
                    }
                case "enterprice-type":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper horizontal-wrapper enterprice-type" + boxed
                        );
                        localStorage.setItem(
                            "page-wrapper",
                            "horizontal-wrapper enterprice-type"
                        );
                        break;
                    }
                case "modern-layout":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-wrapper modern-type" + boxed
                        );
                        localStorage.setItem("page-wrapper", "compact-wrapper modern-type");
                        break;
                    }
                case "material-layout":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper horizontal-wrapper material-type" + boxed
                        );
                        localStorage.setItem(
                            "page-wrapper",
                            "horizontal-wrapper material-type"
                        );

                        break;
                    }
                case "material-icon":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-sidebar compact-small material-icon" + boxed
                        );
                        localStorage.setItem(
                            "page-wrapper",
                            "compact-sidebar compact-small material-icon"
                        );

                        break;
                    }
                case "advance-type":
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper horizontal-wrapper enterprice-type advance-layout" +
                            boxed
                        );
                        localStorage.setItem(
                            "page-wrapper",
                            "horizontal-wrapper enterprice-type advance-layout"
                        );

                        break;
                    }
                default:
                    {
                        $(".page-wrapper").attr(
                            "class",
                            "page-wrapper compact-wrapper " + boxed
                        );
                        localStorage.setItem("page-wrapper", "compact-wrapper");
                        break;
                    }
            }
            // $(this).addClass("active");
            location.reload(true);
        });

        $(".main-layout li").on("click", function() {
            $(".main-layout li").removeClass("active");
            $(this).addClass("active");
            var layout = $(this).attr("data-attr");
            $("body").attr("class", layout);
            $("html").attr("dir", layout);
        });

        $(".main-layout .box-layout").on("click", function() {
            $(".main-layout .box-layout").removeClass("active");
            $(this).addClass("active");
            var layout = $(this).attr("data-attr");
            $("body").attr("class", "box-layout");
            $("html").attr("dir", layout);
        });
    });
})(jQuery);