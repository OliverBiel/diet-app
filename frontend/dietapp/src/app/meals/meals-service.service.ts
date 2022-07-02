import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Meal } from './meal.model';
import { Food } from './food.model';


@Injectable({
  providedIn: 'root'
})
export class MealsServiceService {

  rootUrl = 'http://localhost:4200/api/';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE',
    })
  };

  constructor( private httpClient: HttpClient ) { }

  public getMeals(): Observable<Meal[]>{
    return this.httpClient.get<Meal[]>(this.rootUrl + 'meals/');
  }
  public getFood(id: number): Observable<Food>{
    return this.httpClient.get<Food>(this.rootUrl + 'foods/' + id + '/');
  }
}
