#ifndef _OBSERVER_H
#define _OBSERVER_H

#include <QSharedPointer>
#include <QVariant>
#include <QList>

class Subject;

class Observer
{
    friend class Subject;
public:
    virtual ~Observer(){}
    virtual void update(const int type, const QSharedPointer<const QVariant>& data) = 0;

    bool addObserver(Subject* subject);
    bool removeObserver(Subject* subject);

private:
    class ObserverGuard {
    public:
        ObserverGuard(Subject* subject, Observer* observer);
        ~ObserverGuard();

    private:
        Q_DISABLE_COPY(ObserverGuard);

    private:
        Subject* subject_;
        Observer* observer_;
    };

    QMap<Subject*, QSharedPointer<ObserverGuard> > guards_;
};

template<typename T>
class ObserverUpdateHelper : public Observer
{
public:
    typedef void (T::*FUN)(const int type, const QSharedPointer<const QVariant>& data);

    ObserverUpdateHelper(T* t, FUN fun) : t_(t), fun_(fun) {}
    virtual void update(const int type, const QSharedPointer<const QVariant>& data)
    {
        (t_->*fun_)(type, data);
    }
private:
    T* t_;
    FUN fun_;
};

class DisableSubjectDerived
{
    friend class Subject;
private:
    DisableSubjectDerived(){}
};

//class Observer::ObserverGuard;
class Subject : virtual public DisableSubjectDerived
{
    friend class Observer::ObserverGuard;
public:
    Subject(){}
    void notify(const int type, const QSharedPointer<const QVariant>& data = QSharedPointer<const QVariant>());

private:
    Q_DISABLE_COPY(Subject);

    void addObserver(Observer* observer);
    void removeObserver(Observer* observer);

private:
    QList<Observer*> observers_;
};

#endif //_OBSERVER_H
