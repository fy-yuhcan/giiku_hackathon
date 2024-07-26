import React from 'react';

export default function RecipeButton({label}) {
    return (
      <div className="grid grid-cols-4 gap-4 w-2/3">
        <input type="button" className="border rounded p-2" value={label} />
      </div>
    );
}
