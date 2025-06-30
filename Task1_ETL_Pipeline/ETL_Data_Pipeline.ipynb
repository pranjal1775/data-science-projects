{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a696a0a0-8904-4132-88d8-89800164f00c",
   "metadata": {},
   "source": [
    "# ETL Data Pipeline\n",
    "\n",
    "## Step 1: Import Libraries\n",
    "\n",
    "## Step 2: Extract Data\n",
    "\n",
    "## Step 3: Transform Data (Imputation + Scaling)\n",
    "\n",
    "## Step 4: Load Data (Save to CSV)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ec5fbad9-1a9c-41e7-b684-ddfb4f3311f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.preprocessing import StandardScaler\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "22e9458c-3941-42c1-b3bd-f9ecb56a6ab7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Data:\n",
      "      Name   Age   Salary\n",
      "0    Alice  25.0  50000.0\n",
      "1      Bob   NaN  60000.0\n",
      "2  Charlie  35.0      NaN\n",
      "3    David  40.0  80000.0\n"
     ]
    }
   ],
   "source": [
    "# Simulate some data with missing values\n",
    "data = {\n",
    "    'Name': ['Alice', 'Bob', 'Charlie', 'David'],\n",
    "    'Age': [25, None, 35, 40],\n",
    "    'Salary': [50000, 60000, None, 80000]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "print(\"Original Data:\")\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4c3915d9-72e5-4d76-9a85-f86a4fc3e09c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Transformed Data:\n",
      "      Name       Age    Salary\n",
      "0    Alice -1.543033 -1.234427\n",
      "1      Bob  0.000000 -0.308607\n",
      "2  Charlie  0.308607  0.000000\n",
      "3    David  1.234427  1.543033\n"
     ]
    }
   ],
   "source": [
    "# Fill missing values using the mean\n",
    "imputer = SimpleImputer(strategy='mean')\n",
    "df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])\n",
    "\n",
    "# Scale (normalize) the Age and Salary columns\n",
    "scaler = StandardScaler()\n",
    "df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])\n",
    "\n",
    "print(\"\\nTransformed Data:\")\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "66a4a90d-5d7b-46bc-b08c-7ff1873dd067",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Data saved as 'processed_data.csv'\n"
     ]
    }
   ],
   "source": [
    "# Save the processed data to a CSV file\n",
    "df.to_csv(\"processed_data.csv\", index=False)\n",
    "print(\"\\nData saved as 'processed_data.csv'\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
