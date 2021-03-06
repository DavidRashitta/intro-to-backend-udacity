# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

form="""
    <form method="post">
        <label>Day
        <input type="text" name="day">
        </label>
        <label>Month
        <input type="text" name="month">
        </label>
        <label>Year
        <input type="text" name="year">
        </label>
      <br>
      <br>
      <input type="submit">
    </form>
    """
months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December']


class MainPage(webapp2.RequestHandler):
    def valid_month(month):
        month_abbvs = dict((m[:3].lower(), m) for m in months)
        if month:
            shot_month = month[:3].lower()
            return month_abbvs.get(shot_month)

    def valid_day(day):
        if day and day.isdigit():
            day = int(day)
            if day > 0 and day <= 31:
                return day
    def valid_year(year):
        if year and year.isdigit():
            year = int(year)
            if year > 1950 and year <= 2017:
                return year


    def get(self):
        self.response.out.write(form)
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day   = vaild_day(self.request.get('day'))
        user_year  = valid_year(self.request.get('year'))

        if not (user_year and user_day and user_month):
            self.response.out.write(form)
        else:
            self.response.out.write('Good job!, David.  that\'s toatally valid day')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
