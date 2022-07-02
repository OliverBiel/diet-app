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
  food!: Food;

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

  getFood(id : number){
    this.api.getFood(id).subscribe(data => {
      food: Food;
      this.food = data;
    });
    return this.food;
  };

}
