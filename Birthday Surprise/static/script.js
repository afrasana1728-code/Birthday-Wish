let images = [
    "/static/img1.jpg",
    "/static/img2.jpg",
    "/static/img3.jpg",
    "/static/img4.jpg",
    "/static/img5.jpg",
    "/static/img6.jpg"
];

let i = 0;

function slideShow(){
    let img = document.getElementById("slide");

    if(img){
        img.src = images[i];
        i = (i + 1) % images.length;
    }

    setTimeout(slideShow, 2000);
}

window.onload = slideShow;