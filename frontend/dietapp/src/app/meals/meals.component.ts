import { Component, OnInit } from '@angular/core';
import { Food } from './food.model';
import { Meal } from './meal.model';
import { MealsServiceService } from './meals-service.service';

@Component({
  selector: 'app-meals',
  templateUrl: './meals.component.html',
  styleUrls: ['./meals.component.scss']
})
export class MealsComponent implements OnInit {

  meals!: Meal[];
  foods!: Food[];

  constructor( private api: MealsServiceService ) { 
   }

  ngOnInit(): void {
    this.getMeals();
    this.getFoods();
  }
  
  getMeals(){
    this.api.getMeals().subscribe(data => {
      this.meals = data;
    });
  };

  getFoods(){
    this.api.getFood().subscribe(data => {
      this.foods = data;
    });
    return this.foods;
  };

}
