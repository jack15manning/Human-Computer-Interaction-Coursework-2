    function changeImage() {

        if (document.getElementById("imgClickAndChange").src == "static/dropDown.png") 
        {
            document.getElementById("imgClickAndChange").src = "static/dropUp.png";
        }
        else 
        {
            document.getElementById("imgClickAndChange").src = "static/dropDown.png";
        }    
    }