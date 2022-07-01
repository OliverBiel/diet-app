import { Component, OnInit } from '@angular/core';
import { Meal } from './meal.model';
import { MealsServiceService } from './meals-service.service';

@Component({
  selector: 'app-meals',
  templateUrl: './meals.component.html',
  styleUrls: ['./meals.component.scss']
})
export class MealsComponent implements OnInit {

  meals!: Meal[];

  constructor( private api: MealsServiceService ) { 
   }

  ngOnInit(): void {
    this.getMeals();
  }
  
  getMeals(){
    this.api.getMeals().subscribe(data => {
      this.meals = data;
    });
  };

}
