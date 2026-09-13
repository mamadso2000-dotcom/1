import calendar
from datetime import date, timedelta
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import redirect
from .models import Planet, Event, ObservationPlan
from django.shortcuts import redirect


# mother views
class GalleryView(ListView):
    template_name = 'gallery.html'
    model = Planet


class CalendarView(ListView):
    # basic datas
    template_name = "calendar.html"
    model = Planet

    # is custom date
    def get(self, request, *args, **kwargs):
        # custom date config
        if "year" not in kwargs or "month" not in kwargs:
            today = date.today()
            return redirect('calendar_month', today.year, today.month)
        
        # default date config
        return super().get(request, *args, **kwargs)
    
    # custom context
    def get_context_data(self, **kwargs):
        # default context
        context = super().get_context_data(**kwargs)

        # date datas
        month = self.kwargs["month"]
        year = self.kwargs["year"]

        context['month'] = month
        context['year'] = year

        # previous month
        if month == 1:
            previous_month = 12
            previous_year = year - 1
        else:
            previous_month = month - 1
            previous_year = year

        # next month 
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year

        # month days
        month_days = calendar.monthcalendar(year, month)

        # start and end
        month_start = date(year, month, 1)
        days_in_month = calendar.monthrange(year, month)[1]
        month_end = date(year, month, days_in_month)

        events = Event.objects.filter(
            start_date__lte=month_end,
            end_date__gte=month_start
        )

        events_by_date = {}
        current_date = month_start

        while current_date <= month_end:
            for event in events:
                if event.start_date <= current_date <= event.end_date:
                    events_by_date.setdefault(current_date, [])
                    events_by_date[current_date].append(event)

            current_date += timedelta(days=1)

        calendar_weeks = []
        for week in month_days:
            calendar_week = []
            for day in week:
                if day == 0:
                    calendar_week.append(None)
                    continue
                current_day = date(year, month, day)
                day_events = events_by_date.get(current_day, [])
                day_data = {
                    'day' : day,
                    'date': current_day,
                    'events': day_events
                }
                calendar_week.append(day_data)

            calendar_weeks.append(calendar_week)

        # add datas to context
        context['next_month'] = next_month
        context['next_year'] = next_year
        context['previous_month'] = previous_month
        context['previous_year'] = previous_year

        context['month_days'] = month_days

        context['events'] = events
        context['events_by_date'] = events_by_date
        context['calendar_weeks'] = calendar_weeks

        return context


class PlansView(ListView):
    template_name = 'plans.html'
    model = ObservationPlan
    context_object_name = 'plans'

# son views
class Planet_Detail(DetailView):
    template_name = 'planet_detail.html'
    model = Planet

class CalendarDayView(TemplateView):
    template_name = 'calendar_day.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        day = self.kwargs["day"]
        month = self.kwargs["month"]
        year = self.kwargs["year"]

        
        selected_date = date(year=year, month=month , day=day)
        day_events = Event.objects.filter(start_date__lte=selected_date, end_date__gte=selected_date)
        
        context['selected_date'] = selected_date
        context['day_events'] = day_events

        return context


class PlanDetailView(DetailView):
    template_name = 'plan_detail.html'
    model = ObservationPlan
    context_object_name = 'plan'

    def get_object(self, **kwargs):
        event_id = self.kwargs["event_id"]
        return ObservationPlan.objects.get(event_id=event_id)