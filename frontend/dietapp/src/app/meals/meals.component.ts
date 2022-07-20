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
  foodsNames: {[id: number]: string} = {};

  constructor( private api: MealsServiceService ) { 
   }

  async ngOnInit(): Promise<void> {
    await this.getFoods();
    // await this.getMeals();
    console.log(this.meals);

  }
  
  getMeals(){
    this.api.getMeals().subscribe(data => {
      this.meals = data;
      for(let meal of this.meals) {
        for(let food of meal.foods) {
         food.foods = this.foodsNames[food.foods];
        }
      }
    });
  };

  getFoods(){
    this.api.getFood().subscribe(data => {
      this.foods = data;
      for (let food of this.foods) {
        this.foodsNames[food.id] = food.name;
      }
      this.getMeals();
    });
  };

}
