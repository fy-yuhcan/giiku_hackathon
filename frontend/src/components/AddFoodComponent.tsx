import React from 'react';
import { useContext } from 'react';
import { PageContext } from '../context/pageContext';
import Button from './Button';

export default function AddFoodComponent() {
    const cameraIconUrl: string = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"
    const penIconUrl: string = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    return (
      <>
        <h1>食材の追加</h1>
        <p>食材を追加する方法を選んでください</p>
        <Button pageChangeTo={"AddFoodByImage"} label={"写真で追加"} icon={cameraIconUrl}/>
        <Button pageChangeTo={"AddFoodByImage"} label={"入力する"} icon={penIconUrl}/>
      </>
    );
}