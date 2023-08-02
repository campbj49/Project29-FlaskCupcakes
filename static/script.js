//wiat for the page to load before adding all the cupcakes
$(document).ready(async function(){
    const cupcakes = await axios({
        url: `http://localhost:5000/api/cupcakes`,
        method: "GET",
      });

    for(cupcake of cupcakes.data.cupcakes){
        let new_li = document.createElement("li");
        let image = document.createElement("img");
        new_li.innerHTML = `<p>Flavor: ${cupcake.flavor} Size: ${cupcake.size} Rating: ${cupcake.rating}</p>`;
        image.src = cupcake.image;
        new_li.appendChild(image);
        $("#cupcakes").append(new_li);
    }
})

//Function for handling form submission
$("#add").on("submit", async (e)=>{
    //e.preventDefault();
    console.log();
    await axios({
        url:`http://localhost:5000/api/cupcakes`,
        method: "POST",
        data: {
            "flavor": $("#flavor").val(),
            "size": $("#size").val(),
            "rating": $("#rating").val(),
            "image": $("#image").val()
        },
    })
})