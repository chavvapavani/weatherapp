import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  displaycity:String="";
  city:String="" ;
  isDisplay = true;
  toggleDisplay(){
    if(this.city!="")
    {
    this.isDisplay = false;
    this.displaycity=this.city;
    }
    else{
      this.isDisplay=true;
    }

  }



}
