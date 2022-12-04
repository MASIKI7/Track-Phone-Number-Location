{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tanzania\n",
      "Airtel\n"
     ]
    }
   ],
   "source": [
    "import phonenumbers\n",
    "number = \"+255782719525\"\n",
    "\n",
    "from phonenumbers import geocoder\n",
    "\n",
    "checknumber = phonenumbers.parse(number,\"CH\")\n",
    "print(geocoder.description_for_number(checknumber,\"en\"))\n",
    "\n",
    "from phonenumbers import carrier\n",
    "\n",
    "servicenumber = phonenumbers.parse(number,\"RO\")\n",
    "print(carrier.name_for_number(servicenumber,\"en\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
