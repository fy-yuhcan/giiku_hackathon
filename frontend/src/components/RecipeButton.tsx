import React from 'react';

export default function RecipeButton({ShowRecipe, record}) {
    return (
      <div className="grid grid-cols-4 gap-4 w-2/3" onClick={() => ShowRecipe(record.recipe_id)}>
        <input type="button" className="border rounded p-2" value={record.title} />
      </div>
    );
}
