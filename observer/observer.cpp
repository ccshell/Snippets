#include "observer.h"

bool Observer::addObserver(Subject* subject)
{
    if (guards_.contains(subject))
        return false;

    guards_[subject]=QSharedPointer<ObserverGuard>(new ObserverGuard(subject, this));
    return true;
}

bool Observer::removeObserver(Subject* subject)
{
    QMap<Subject*, QSharedPointer<ObserverGuard> >::iterator it = guards_.find(subject);
    if (it != guards_.end())
    {
        guards_.erase(it);
        return true;
    }
    return false;
}

Observer::ObserverGuard::ObserverGuard(Subject* subject, Observer* observer) :
subject_(subject),
    observer_(observer)
{
    subject_->addObserver(observer_);
}

Observer::ObserverGuard::~ObserverGuard()
{
    subject_->removeObserver(observer_);
}

void Subject::addObserver(Observer* observer)
{
    if (!observers_.contains(observer))
    {
        observers_.push_back(observer);
    }
}

void Subject::removeObserver(Observer* observer)
{
    observers_.removeOne(observer);
}

void Subject::notify(const int type, const QSharedPointer<const QVariant>& data)
{
    for (QList<Observer*>::iterator i = observers_.begin(); i != observers_.end(); ++i)
    {
        (*i)->update(type, data);
    }
}
