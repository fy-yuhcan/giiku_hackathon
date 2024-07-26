import React from 'react';
import Button from './Button';

export default function HomeComponent() {
    const cartIconUrl: string = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    const cookingIconUrl: string = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"

    return (
      <>
        <img src="../img/shokumane.png" alt="shokumane.png"></img>
        <Button pageChangeTo={"AddFoodByImage"} label={"写真で追加"} icon={cartIconUrl}/>
        <Button pageChangeTo={"AddFoodByImage"} label={"入力する"} icon={cookingIconUrl}/>
      </>
    );
}