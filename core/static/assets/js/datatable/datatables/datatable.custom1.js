(function($) {
    $(document).ready(function() {
        // // Setup - add a text input to each footer cell

        //single row delete data table start here
        var deleterow = $("#row-select-delete").DataTable();
        $("#row-select-delete tbody").on("click", "tr", function() {
            if ($(this).hasClass("selected")) {
                $(this).removeClass("selected");
            } else {
                deleterow.$("tr.selected").removeClass("selected");
                $(this).addClass("selected");
            }
        });
        //single row delete data table end here

        //Range plugin datatable start here
        $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
            var min = parseInt($("#min").val(), 10);
            var max = parseInt($("#max").val(), 10);
            var age = parseFloat(data[3]) || 0;
            if (
                (isNaN(min) && isNaN(max)) ||
                (isNaN(min) && age <= max) ||
                (min <= age && isNaN(max)) ||
                (min <= age && age <= max)
            ) {
                return true;
            }
            return false;
        });
        var dtage = $("#datatable-range").DataTable();
        $("#min, #max").keyup(function() {
            dtage.draw();
        });
        //Range plugin datatable end here
    });
    /* Formatting function for row details - modify as you need */
    function format(d) {
        // `d` is the original data object for the row
        return (
            '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">' +
            "<tr>" +
            "<td>Full name:</td>" +
            "<td>" +
            d.name +
            "</td>" +
            "</tr>" +
            "<tr>" +
            "<td>Extension number:</td>" +
            "<td>" +
            d.extn +
            "</td>" +
            "</tr>" +
            "<tr>" +
            "<td>Extra info:</td>" +
            "<td>And any further details here (images etc)...</td>" +
            "</tr>" +
            "</table>"
        );
    }

    $(document).ready(function() {
        // row create
        $("#row_create").DataTable({
            createdRow: function(row, data, index) {
                if (data[5].replace(/[\$,]/g, "") * 1 > 150000) {
                    $("td", row).eq(5).addClass("highlight");
                } else if (data[5].replace(/[\$,]/g, "") * 1 < 40000) {
                    $("td", row).eq(5).addClass("danger");
                }
            },
        });
    });
    // stock result chart
    $(document).ready(function() {
        var stock_data = [{
                name: "ACME Gadgets",
                symbol: "AGDTS",
                last: [2.57, 2.54, 2.54, 2.56, 2.57, 2.58, 2.59],
            },
            {
                name: "Spry Media Productions",
                symbol: "SPMP",
                last: [1.12, 1.11, 1.08, 1.08, 1.09, 1.11, 1.08],
            },
            {
                name: "Widget Emporium",
                symbol: "WDEMP",
                last: [3.4, 3.39, 3.46, 3.51, 3.5, 3.48, 3.49],
            },
            {
                name: "Sole Goodman",
                symbol: "SGMAN",
                last: [16.2, 16.4, 16.36, 16.35, 16.61, 16.46, 16.19],
            },
            {
                name: "Stanler Bits and Bobs",
                symbol: "SBIBO",
                last: [82.51, 83.47, 83.4, 83.68, 83.81, 83.29, 83.72],
            },
        ];

        let table = $("#stock").DataTable({
            ajax: function(dataSent, callback, settings) {
                let data = stock_charts;
                if (data == undefined) {
                    data = stock_data;
                } else {
                    data = data.data;
                    for (i = 0; i < data.length; i++) {
                        data[i].last.push(data[i].last.shift());
                    }
                }

                callback({
                    data: data
                });
            },
            paging: false,
            initComplete: function() {
                let api = this.api();
                setInterval(function() {
                    api.ajax.reload();
                }, 5000);
            },
            drawCallback: function() {
                $(".sparkline")
                    .map(function() {
                        return $("canvas", this).length ? null : this;
                    })
                    .sparkline("html", {
                        type: "line",
                        width: "250px",
                    });
            },
            columns: [{
                    data: "name",
                },
                {
                    data: "symbol",
                },
                {
                    data: null,
                    render: function(data, type, row, meta) {
                        return row.last[row.last.length - 1].toFixed(2);
                    },
                },
                {
                    data: null,
                    render: function(data, type, row, meta) {
                        var val = (
                            row.last[row.last.length - 1] - row.last[row.last.length - 2]
                        ).toFixed(2);
                        var colour = val < 0 ? "red" : "green";
                        return type === "display" ?
                            '<span style="color:' + colour + '">' + val + "</span>" :
                            val;
                    },
                },
                {
                    data: "last",
                    render: function(data, type, row, meta) {
                        return type === "display" ?
                            '<span class="sparkline">' + data.toString() + "</span>" :
                            data;
                    },
                },
            ],
        });
    });
    var stock_charts = {
        data: [{
                name: "ACME Gadgets",
                symbol: "AGDTS",
                last: [2.56, 2.57, 2.58, 2.59, 2.57, 2.54, 2.54],
            },
            {
                name: "Spry Media Productions",
                symbol: "SPMP",
                last: [1.08, 1.09, 1.11, 1.08, 1.12, 1.11, 1.08],
            },
            {
                name: "Widget Emporium",
                symbol: "WDEMP",
                last: [3.51, 3.5, 3.48, 3.49, 3.4, 3.39, 3.46],
            },
            {
                name: "Sole Goodman",
                symbol: "SGMAN",
                last: [16.35, 16.61, 16.46, 16.19, 16.2, 16.4, 16.36],
            },
            {
                name: "Stanler Bits and Bobs",
                symbol: "SBIBO",
                last: [83.68, 83.81, 83.29, 83.72, 82.51, 83.47, 83.4],
            },
        ],
    };
})(jQuery);