/* CLASES */

class Preloader{
    preloader = "";

    constructor(){
        this.preloader = document.getElementById('preload');

        this.load();
    }

    load(){
        window.addEventListener('load', ()=>{
            this.preloader.style.display = 'none';
        });
    }
}

class Menu{
    menu = "";
    menuOpen = "";
    menuClose = "";

    constructor(){
        this.menu = document.getElementById('mobile-menu');
        this.menuOpen = document.getElementById('menu-open');
        this.menuClose = document.getElementById('menu-close');
        
        this.openMenu();
        this.closeMenu();
    }

    openMenu(){
        this.menuOpen.addEventListener('click', ()=>{
            this.menu.classList.remove("mobile-menu-close");
            this.menuOpen.style.display = 'none';
            this.menuClose.style.display = 'flex';
            window.setTimeout(()=>{
                this.menu.classList.add('mobile-menu-show');
            },500);
        });
    }

    closeMenu(){
        this.menuClose.addEventListener('click', ()=>{
            this.menu.classList.add('mobile-menu-close');
            this.menuClose.style.display = 'none';
            this.menuOpen.style.display = 'flex';
        });
    }
}

/* OBJETOS */
//var load = new Preloader();
var menu = new Menu();